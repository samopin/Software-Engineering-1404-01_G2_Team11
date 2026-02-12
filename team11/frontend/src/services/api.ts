import axios from 'axios';
import { CreateTripPayload, UpdateTripItemPayload } from '@/types/trip';

const api = axios.create({
    baseURL: '/api',
    headers: {
        'Content-Type': 'application/json',
    },
});

export const destinationApi = {
    suggest: (data: any) => api.post('/destinations', data),
};

export const tripApi = {
    create: (data: CreateTripPayload) => api.post('/trips', data),
    getById: (id: string) => api.get(`/trips/${id}`),
    updateItem: (tripId: string, itemId: string, data: UpdateTripItemPayload) => 
        api.patch(`/trips/${tripId}/items/${itemId}`, data),
    deleteItem: (tripId: string, itemId: string) => 
        api.delete(`/trips/${tripId}/items/${itemId}`),
    suggestAlternative: (tripId: string, itemId: string) => 
        api.post(`/trips/${tripId}/items/${itemId}/suggest-alternative`),
};

export default api;