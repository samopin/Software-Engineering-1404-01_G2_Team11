import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useApi } from '@/hooks/useApi';
import { tripApi } from '@/services/api';
import { getMockTrip } from '@/services/mockService';
import { Trip } from '@/types/trip';
import Timeline from '@/components/Timeline';
import Button from '@/components/ui/Button';

const FinalizeTrip: React.FC = () => {
    console.log('ffff')
  const { tripId } = useParams<{ tripId: string }>();
  const navigate = useNavigate();
  
  const [tripData, setTripData] = useState<Trip | null>(null);
  const { data, isLoading, error, request } = useApi(getMockTrip);

  useEffect(() => {
    if (tripId) {
      request(tripId);
    }
  }, [tripId]);

  useEffect(() => {
    if (data) {
      setTripData(data);
    }
  }, [data]);

  const handleItemTimeChange = async (itemId: string, startTime: string, endTime: string) => {
    if (!tripId) return;

    try {
      await tripApi.updateItem(tripId, itemId, {
        start_time: startTime,
        end_time: endTime,
      });

      // Update local state
      setTripData((prev) => {
        if (!prev) return prev;
        return {
          ...prev,
          days: prev.days.map((day) => ({
            ...day,
            items: day.items.map((item) =>
              item.id === itemId
                ? { ...item, start_time: startTime, end_time: endTime }
                : item
            ),
          })),
        };
      });
    } catch (err) {
      console.error('Failed to update item time:', err);
      alert('خطا در به‌روزرسانی زمان. لطفاً دوباره تلاش کنید.');
    }
  };

  const handleDeleteItem = async (itemId: string) => {
    if (!tripId) return;

    const confirmed = window.confirm('آیا از حذف این آیتم اطمینان دارید؟');
    if (!confirmed) return;

    try {
      await tripApi.deleteItem(tripId, itemId);

      // Update local state
      setTripData((prev) => {
        if (!prev) return prev;
        return {
          ...prev,
          days: prev.days.map((day) => ({
            ...day,
            items: day.items.filter((item) => item.id !== itemId),
          })),
        };
      });
    } catch (err) {
      console.error('Failed to delete item:', err);
      alert('خطا در حذف آیتم. لطفاً دوباره تلاش کنید.');
    }
  };

  const handleSuggestAlternative = async (itemId: string) => {
    if (!tripId) return;

    try {
      const response = await tripApi.suggestAlternative(tripId, itemId);
      const alternativeItem = response.data;

      // Update local state with alternative item
      setTripData((prev) => {
        if (!prev) return prev;
        return {
          ...prev,
          days: prev.days.map((day) => ({
            ...day,
            items: day.items.map((item) =>
              item.id === itemId ? alternativeItem : item
            ),
          })),
        };
      });

      alert('آیتم جایگزین با موفقیت پیشنهاد شد.');
    } catch (err) {
      console.error('Failed to suggest alternative:', err);
      alert('خطا در پیشنهاد آیتم جایگزین. لطفاً دوباره تلاش کنید.');
    }
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">در حال بارگذاری...</p>
        </div>
      </div>
    );
  }

  if (error || !tripData) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center">
          <i className="fa-solid fa-exclamation-circle text-red-500 text-4xl mb-4"></i>
          <p className="text-red-600 mb-4">{error || 'برنامه سفر یافت نشد'}</p>
          <Button onClick={() => navigate('/')} variant="primary">
            بازگشت به صفحه اصلی
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h1 className="text-3xl font-bold text-gray-900 mb-2">
              {tripData.title}
            </h1>
            <div className="flex items-center gap-4 text-sm text-gray-600">
              <span>
                <i className="fa-solid fa-location-dot ml-1"></i>
                {tripData.city}, {tripData.province}
              </span>
              <span>
                <i className="fa-solid fa-calendar ml-1"></i>
                {tripData.start_date} تا {tripData.end_date}
              </span>
              <span>
                <i className="fa-solid fa-clock ml-1"></i>
                {tripData.duration_days} روز
              </span>
              <span className="font-bold text-green-600">
                <i className="fa-solid fa-coins ml-1"></i>
                {tripData.total_cost.toLocaleString('fa-IR')} تومان
              </span>
            </div>
          </div>
          <div className="flex gap-2">
            <Button
              onClick={() => navigate('/')}
              variant="secondary"
            >
              <i className="fa-solid fa-arrow-right ml-2"></i>
              بازگشت
            </Button>
            <Button
              onClick={() => alert('ذخیره تغییرات')}
              variant="primary"
            >
              <i className="fa-solid fa-save ml-2"></i>
              ذخیره نهایی
            </Button>
          </div>
        </div>

        {/* Trip Info */}
        <div className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-lg p-4 flex items-center justify-between">
          <div className="flex gap-6 text-sm">
            <span className="px-3 py-1 bg-white rounded-full shadow-sm">
              <i className="fa-solid fa-user-group ml-1 text-blue-600"></i>
              {tripData.style}
            </span>
            <span className="px-3 py-1 bg-white rounded-full shadow-sm">
              <i className="fa-solid fa-wallet ml-1 text-green-600"></i>
              {tripData.budget_level}
            </span>
            <span className="px-3 py-1 bg-white rounded-full shadow-sm">
              <i className="fa-solid fa-circle-check ml-1 text-purple-600"></i>
              {tripData.status}
            </span>
          </div>
        </div>
      </div>

      {/* Timelines */}
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-gray-800 mb-6">
          طرح پیشنهادی سفر
        </h2>
        
        {tripData.days.map((day) => (
          <Timeline
            key={day.day_number}
            date={day.date}
            dayNumber={day.day_number}
            items={day.items}
            onItemTimeChange={handleItemTimeChange}
            onDeleteItem={handleDeleteItem}
            onSuggestAlternative={handleSuggestAlternative}
          />
        ))}

        {tripData.days.length === 0 && (
          <div className="text-center py-12 text-gray-500">
            <i className="fa-solid fa-calendar-xmark text-4xl mb-4"></i>
            <p>هنوز برنامه‌ای برای این سفر تعریف نشده است.</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default FinalizeTrip;
