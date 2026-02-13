import React, { useState } from 'react';
import { AlternativePlace, CategoryType } from '@/types/trip';
import { formatPersianCurrency } from '@/utils/costCalculations';
import {
    Dialog,
    DialogContent,
    DialogHeader,
    DialogTitle,
    DialogDescription,
} from '@/components/ui/dialog';
import Button from './Button';

interface AlternativesDialogProps {
    isOpen: boolean;
    onClose: () => void;
    alternatives: AlternativePlace[];
    currentPlaceTitle: string;
    onSelectAlternative: (placeId: string) => void;
    isLoading?: boolean;
}

const getCategoryLabel = (category: CategoryType): string => {
    const labels: Record<CategoryType, string> = {
        HISTORICAL: 'تاریخی',
        SHOPPING: 'خرید',
        RECREATIONAL: 'تفریحی',
        RELIGIOUS: 'مذهبی',
        NATURAL: 'طبیعی',
        DINING: 'غذا',
        STUDY: 'آموزشی',
        EVENTS: 'رویداد'
    };
    return labels[category] || category;
};

const AlternativesDialog: React.FC<AlternativesDialogProps> = ({
    isOpen,
    onClose,
    alternatives,
    currentPlaceTitle,
    onSelectAlternative,
    isLoading = false
}) => {
    const [selectedId, setSelectedId] = useState<string | null>(null);

    const handleSubmit = () => {
        if (selectedId) {
            onSelectAlternative(selectedId);
        }
    };

    return (
        <Dialog open={isOpen} onOpenChange={(open) => { if (!open) onClose(); }}>
            <DialogContent className="max-w-4xl max-h-[80vh] overflow-hidden flex flex-col p-0 my-4 m-h-[80vh]">
                <DialogHeader className="px-6 pt-6 pb-4 border-b border-gray-200 flex-row justify-between">
                    <DialogTitle className="text-xl font-bold text-gray-900 ms-8">پیشنهاد جایگزین</DialogTitle>
                    <DialogDescription className="text-sm text-gray-600 me-9 mt-1">
                        جایگزین برای: <span className="font-semibold">{currentPlaceTitle}</span>
                    </DialogDescription>
                </DialogHeader>

                {/* Content */}
                <div className="flex-1 overflow-y-auto px-6 py-0">
                    {isLoading && alternatives.length === 0 ? (
                        <div className="text-center py-6">
                            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
                            <p className="text-gray-600 font-medium">در حال دریافت پیشنهادات...</p>
                        </div>
                    ) : alternatives.length === 0 ? (
                        <div className="text-center py-6 text-gray-500">
                            <svg className="w-16 h-16 mx-auto mb-4 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
                            </svg>
                            <p>جایگزینی یافت نشد</p>
                        </div>
                    ) : (
                        <div className="space-y-3">
                            {alternatives.map((alt) => (
                                <div
                                    key={alt.id}
                                    onClick={() => !isLoading && setSelectedId(alt.id)}
                                    className={`
                                        p-5 border-2 rounded-lg cursor-pointer transition-all
                                        ${selectedId === alt.id
                                            ? 'border-persian-gold bg-yellow-50'
                                            : 'border-gray-200 hover:border-persian-gold/50 hover:bg-gray-50'
                                        }
                                        ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}
                                    `}
                                >
                                    <div className="flex justify-between items-start mb-0 gap-4 mb-0">
                                        <div className="flex-1 space-y-3">
                                            {/* Row 1: Title, Category, Entry Fee, Rating */}
                                            <div className="flex items-center justify-between gap-4 flex-wrap">
                                                <div className="flex items-center gap-3 flex-1">
                                                    <h3 className="text-lg font-bold text-gray-900">{alt.title}</h3>
                                                    <span className="px-2.5 py-1 text-xs font-medium rounded-full bg-blue-100 text-blue-800">
                                                        {getCategoryLabel(alt.category)}
                                                    </span>
                                                </div>

                                                <div className="flex items-center gap-4 flex-shrink-0">
                                                    {alt.entry_fee !== undefined && (
                                                        <div className="flex items-center gap-1.5 text-gray-700">
                                                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                                            </svg>
                                                            <span className="text-sm font-semibold">
                                                                {alt.entry_fee === 0 ? 'رایگان' : formatPersianCurrency(alt.entry_fee)}
                                                            </span>
                                                        </div>
                                                    )}

                                                    {alt.rating && (
                                                        <div className="flex items-center gap-1.5 text-yellow-600">
                                                            <svg className="w-5 h-5 fill-current" viewBox="0 0 20 20">
                                                                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                                                            </svg>
                                                            <span className="text-sm font-bold">{alt.rating.toFixed(1)}</span>
                                                        </div>
                                                    )}
                                                </div>
                                            </div>

                                            {/* Row 2: Recommendation Reason */}
                                            {alt.recommendation_reason && (
                                                <div className="flex items-start mb-0 gap-2">
                                                    <span className="text-lg">💡</span>
                                                    <p className="text-sm text-gray-700 font-medium flex-1">
                                                        {alt.recommendation_reason}
                                                    </p>
                                                </div>
                                            )}

                                            {/* Row 3: Address (smaller) */}
                                            {alt.address && (
                                                <div className="flex items-start mb-0 gap-2">
                                                    <svg className="w-3.5 h-3.5 mt-0.5 flex-shrink-0 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                                                    </svg>
                                                    <span className="text-xs text-gray-500">{alt.address}</span>
                                                </div>
                                            )}
                                        </div>

                                        {/* Selection Indicator */}
                                        {selectedId === alt.id && !isLoading && (
                                            <div className="flex-shrink-0 text-persian-gold">
                                                <svg className="w-7 h-7" fill="currentColor" viewBox="0 0 20 20">
                                                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                                                </svg>
                                            </div>
                                        )}
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>

                {/* Footer */}
                <div className="px-6 py-4 border-t border-gray-200 bg-gray-50 flex justify-end gap-3">
                    <Button
                        variant='cancel'
                        onClick={onClose}
                        disabled={isLoading}
                        className='rounded-md '
                    >
                        انصراف
                    </Button>
                    <Button
                        variant='cta'
                        onClick={handleSubmit}
                        disabled={!selectedId || isLoading}
                        className='rounded-md '
                    >
                        تایید
                    </Button>
                </div>

                {/* Loading Overlay - Only shown during replacement */}
                {isLoading && alternatives.length > 0 && (
                    <div className="absolute inset-0 bg-white bg-opacity-90 flex items-center justify-center rounded-lg">
                        <div className="flex flex-col items-center gap-3">
                            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-persian-gold"></div>
                            <p className="text-gray-700 font-semibold">در حال جایگزینی...</p>
                        </div>
                    </div>
                )}
            </DialogContent>
        </Dialog>
    );
};

export default AlternativesDialog;
