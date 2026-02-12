import React, { useMemo } from 'react';
import MultiRangeSlider, { RangeSection } from '@/components/ui/MultiRangeSlider';
import TripItemCard from '@/components/TripItemCard';
import { TripItem } from '@/types/trip';

interface TimelineProps {
  date: string;
  dayNumber: number;
  items: TripItem[];
  onItemTimeChange: (itemId: string, startTime: string, endTime: string) => void;
  onDeleteItem: (itemId: string) => void;
  onSuggestAlternative: (itemId: string) => void;
}

// Constants for timeline visualization
const MINUTES_PER_PIXEL = 0.5; // 0.5 minute per pixel (larger timeline)
const CARD_MAX_WIDTH = 500;
const TIMELINE_START_HOUR = 0; // 00:00
const TIMELINE_END_HOUR = 24; // 24:00

const Timeline: React.FC<TimelineProps> = ({
  date,
  dayNumber,
  items,
  onItemTimeChange,
  onDeleteItem,
  onSuggestAlternative,
}) => {
  // Convert time string (HH:MM) to minutes from midnight
  const timeToMinutes = (time: string): number => {
    const [hours, minutes] = time.split(':').map(Number);
    return hours * 60 + minutes;
  };

  // Convert minutes to time string (HH:MM)
  const minutesToTime = (minutes: number): string => {
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return `${hours.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}`;
  };

  // Calculate total timeline in minutes (24 hours)
  const totalMinutes = (TIMELINE_END_HOUR - TIMELINE_START_HOUR) * 60;
  
  // Calculate total timeline width in pixels
  const timelineWidth = totalMinutes / MINUTES_PER_PIXEL;

  // Separate items by type
  const visitItems = useMemo(() => items.filter((item) => item.type === 'VISIT'), [items]);
  const stayItems = useMemo(() => items.filter((item) => item.type === 'STAY'), [items]);

  // Convert items to range sections for VISIT
  const visitRangeSections: RangeSection[] = useMemo(() => {
    return visitItems.map((item) => ({
      start: timeToMinutes(item.start_time),
      end: timeToMinutes(item.end_time),
    }));
  }, [visitItems]);

  // Convert items to range sections for STAY
  const stayRangeSections: RangeSection[] = useMemo(() => {
    return stayItems.map((item) => ({
      start: timeToMinutes(item.start_time),
      end: timeToMinutes(item.end_time),
    }));
  }, [stayItems]);

  // Handle range changes for VISIT
  const handleVisitRangeChange = (sections: RangeSection[]) => {
    sections.forEach((section, index) => {
      const item = visitItems[index];
      if (item) {
        const newStartTime = minutesToTime(section.start);
        const newEndTime = minutesToTime(section.end);
        
        if (newStartTime !== item.start_time || newEndTime !== item.end_time) {
          onItemTimeChange(item.id, newStartTime, newEndTime);
        }
      }
    });
  };

  // Handle range changes for STAY
  const handleStayRangeChange = (sections: RangeSection[]) => {
    sections.forEach((section, index) => {
      const item = stayItems[index];
      if (item) {
        const newStartTime = minutesToTime(section.start);
        const newEndTime = minutesToTime(section.end);
        
        if (newStartTime !== item.start_time || newEndTime !== item.end_time) {
          onItemTimeChange(item.id, newStartTime, newEndTime);
        }
      }
    });
  };

  // Calculate card positions and widths for an item array
  const calculateCardPositions = (itemArray: TripItem[]) => {
    return itemArray.map((item) => {
      const startMinutes = timeToMinutes(item.start_time);
      const endMinutes = timeToMinutes(item.end_time);
      const durationMinutes = endMinutes - startMinutes;
      // Use exact same formula for both width and position
      let width = durationMinutes / MINUTES_PER_PIXEL;
      if (width > CARD_MAX_WIDTH)
        width = CARD_MAX_WIDTH
      const translateX = endMinutes  / MINUTES_PER_PIXEL - width;
      console.log(translateX, width)


      return { width, translateX };
    });
  };

  const visitCardPositions = useMemo(() => calculateCardPositions(visitItems), [visitItems]);
  const stayCardPositions = useMemo(() => calculateCardPositions(stayItems), [stayItems]);

  // Render a single timeline track
  const renderTimelineTrack = (
    title: string,
    itemArray: TripItem[],
    rangeSections: RangeSection[],
    cardPositions: { width: number; translateX: number }[],
    handleRangeChange: (sections: RangeSection[]) => void,
    color: string
  ) => {
    if (itemArray.length === 0) return null;

    return (
      <div className="mb-8">
        <h3 className="text-sm font-semibold text-gray-700 mb-3">{title}</h3>
        <div className="relative" style={{ width: '100%', overflowX: 'auto', overflowY: 'visible' }}>
          <div style={{ width: `${timelineWidth}px`, minWidth: '100%', position: 'relative' }}>
            {/* Cards Container */}
            <div className="relative mb-4" style={{ height: '220px' }}>
              {itemArray.map((item, index) => {
                const { width, translateX } = cardPositions[index];
                return (
                  <div
                    key={item.id}
                    className="absolute top-0 left-0"
                    style={{ 
                      transform: `translateX(${translateX}px)`,
                      transition: 'transform 0.2s ease'
                    }}
                  >
                    <TripItemCard
                      item={item}
                      width={width}
                      maxWidth={CARD_MAX_WIDTH}
                      onDelete={onDeleteItem}
                      onSuggestAlternative={onSuggestAlternative}
                    />
                  </div>
                );
              })}
            </div>

            {/* Slider with custom thumbs showing time */}
            <MultiRangeSlider
              sections={rangeSections}
              min={0}
              max={totalMinutes}
              step={15}
              onChange={handleRangeChange}
              activeColor={color}
              gapColor="#e2e8f0"
              renderThumb={(params: any) => {
                const item = itemArray[params.sectionIndex];
                const time = params.isStartThumb ? item?.start_time : item?.end_time;

                return (
                  <div
                    {...params.props}
                    key={params.props.key}
                    style={{
                      ...params.props.style,
                      height: '32px',
                      width: '32px',
                      borderRadius: '50%',
                      backgroundColor: '#FFF',
                      boxShadow: '0px 2px 8px rgba(0,0,0,0.25)',
                      display: 'flex',
                      justifyContent: 'center',
                      alignItems: 'center',
                      cursor: 'grab',
                      outline: 'none',
                      border: `2px solid ${color}`,
                    }}
                  >
                    <div
                      className="absolute top-full mt-2 text-xs font-semibold text-gray-700 whitespace-nowrap"
                      style={{ pointerEvents: 'none' }}
                    >
                      {time}
                    </div>
                  </div>
                );
              }}
            />

            {/* Time markers */}
            <div className="flex justify-between mt-2 text-xs text-gray-400">
              {[0, 4, 8, 12, 16, 20, 24].map((hour) => (
                <span key={hour}>{hour.toString().padStart(2, '0')}:00</span>
              ))}
            </div>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="mb-12">
      {/* Day Header */}
      <div className="mb-6 pb-4 border-b-2 border-gray-200">
        <div className="flex items-center gap-2">
          <span className="text-2xl font-bold text-gray-800">روز {dayNumber}</span>
          <span className="text-base text-gray-500">{date}</span>
        </div>
      </div>

      {/* VISIT Timeline */}
      {renderTimelineTrack(
        'برنامه بازدید',
        visitItems,
        visitRangeSections,
        visitCardPositions,
        handleVisitRangeChange,
        '#276EF1'
      )}

      {/* STAY Timeline */}
      {renderTimelineTrack(
        'زمان‌بندی اقامت',
        stayItems,
        stayRangeSections,
        stayCardPositions,
        handleStayRangeChange,
        '#9333EA'
      )}

      {visitItems.length === 0 && stayItems.length === 0 && (
        <div className="text-center py-8 text-gray-400">
          <p>برنامه‌ای برای این روز تعریف نشده است</p>
        </div>
      )}
    </div>
  );
};

export default Timeline;
