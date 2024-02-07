import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { BookingService } from './booking.service';

@Component({
  selector: 'app-booking',
  templateUrl: './booking.component.html',
  styleUrls: ['./booking.component.scss']
})
export class BookingComponent implements OnInit {
  bookingForm: FormGroup;
  customers: any[] = [];
  roomId!: number; 
  roomAvailability: any[] = []; 

  constructor(
    private formBuilder: FormBuilder,
    private bookingService: BookingService,
    private route: ActivatedRoute
  ) {
    this.bookingForm = this.formBuilder.group({
      customerId: ['', Validators.required],
      checkInDate: ['', Validators.required],
      checkOutDate: ['', Validators.required],
      price: [''], 
      days: [''] 
    });
  }

  ngOnInit(): void {
    this.roomId = this.route.snapshot.params['roomId'];
    this.loadCustomers();
    this.loadRoomAvailability();
  }

  loadCustomers() {
    this.bookingService.getCustomers().subscribe((data: any) => {
      this.customers = data;
    }, (error: any) => {
      console.error('Error fetching customers:', error);
    });
  }
  
  loadRoomAvailability() {
    this.bookingService.getRoomAvailability().subscribe((data: any) => {
      this.roomAvailability = data;
    }, (error) => {
      console.error('Error fetching room availability:', error);
    });
  }

  onSubmit() {
    const checkInDate = this.bookingForm.get('checkInDate')?.value;
    const checkOutDate = this.bookingForm.get('checkOutDate')?.value;

    const oneDay = 24 * 60 * 60 * 1000;
    const checkInTime = new Date(checkInDate).getTime();
    const checkOutTime = new Date(checkOutDate).getTime();
    const numberOfDays = Math.round(Math.abs((checkOutTime - checkInTime) / oneDay));

    const roomId = this.roomId;
    const room = this.roomAvailability.find((room: any) => room.roomId === roomId);
    if (!room) {
      console.error('Room not found.');
      return;
    }
    const roomPrice = room.price;

    const totalPrice = numberOfDays * roomPrice;


    this.bookingForm.patchValue({
      price: totalPrice
    });

    this.bookingService.createBooking(this.bookingForm.value).subscribe((response: any) => {
      console.log('Booking created successfully:', response);
    }, (error) => {
      console.error('Error creating booking:', error);
    });
  }
}
