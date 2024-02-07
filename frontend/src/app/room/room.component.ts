import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { RoomService } from './room.service';

@Component({
  selector: 'app-room',
  templateUrl: './room.component.html',
  styleUrls: ['./room.component.scss']
})
export class RoomComponent implements OnInit {
  roomAvailability: any[] = [];

  constructor(private roomService: RoomService, private router: Router) { }

  ngOnInit(): void {
    this.loadRoomAvailability();
  }

  loadRoomAvailability() {
    this.roomService.getRoomAvailability().subscribe((data: any) => {
      this.roomAvailability = data;
    }, (error) => {
      console.error('Error fetching room availability:', error);
    });
  }

  getRoomTypeName(roomTypeId: number): string {
    switch (roomTypeId) {
      case 1:
        return 'Standard';
      case 2:
        return 'Deluxe';
      case 3:
        return 'Suite';
      case 4:
        return 'Executive Suite';
      default:
        return 'Unknown'; // Handle unknown room types
    }
  }

  bookRoom(roomId: number) {
    console.log('Booking room with ID:', roomId);
    this.router.navigate(['/booking', { roomId: roomId }]);
  }
}
