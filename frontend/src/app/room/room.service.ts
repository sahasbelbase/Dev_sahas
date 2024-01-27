import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RoomService {
  
  roomAvailabilityData = [
    { roomNumber: '101', availability: 'Available' },
    { roomNumber: '102', availability: 'Occupied' },
    { roomNumber: '103', availability: 'Available' },
    
  ];

  constructor() {}

  getRoomAvailability(): any[] {
    return this.roomAvailabilityData;
  }
}
