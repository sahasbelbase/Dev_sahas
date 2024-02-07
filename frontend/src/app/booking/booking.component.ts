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
  roomId!: number; // Initialize roomId here or use '!' operator
  roomAvailability: any[] = []; // Add roomAvailability property

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
    this.roomId = this.route.snapshot.params['roomId']; // Get roomId from route parameters
    this.loadCustomers();
    this.loadRoomAvailability();
  }

  loadCustomers() {
    this.bookingService.getCustomers().subscribe((data: any) => {
      this.customers = data;
    }, (error: any) => { // Explicitly type the error parameter
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
    // Get check-in and check-out dates from the form
    const checkInDate = this.bookingForm.get('checkInDate')?.value;
    const checkOutDate = this.bookingForm.get('checkOutDate')?.value;

    // Calculate the number of days between check-in and check-out dates
    const oneDay = 24 * 60 * 60 * 1000; // hours * minutes * seconds * milliseconds
    const checkInTime = new Date(checkInDate).getTime();
    const checkOutTime = new Date(checkOutDate).getTime();
    const numberOfDays = Math.round(Math.abs((checkOutTime - checkInTime) / oneDay));

    // Fetch the price from the room based on the selected room ID
    const roomId = this.roomId; // Use the roomId property
    const room = this.roomAvailability.find((room: any) => room.roomId === roomId); // Provide type for room parameter
    if (!room) {
      console.error('Room not found.');
      return;
    }
    const roomPrice = room.price; // Assuming the price is directly available in the room object

    // Calculate the total price based on the room price and number of days
    const totalPrice = numberOfDays * roomPrice;

    // Update the price and days fields in the form
    this.bookingForm.patchValue({
      price: totalPrice,
      days: numberOfDays
    });

    // Submit the booking form
    this.bookingService.createBooking(this.bookingForm.value).subscribe((response: any) => {
      console.log('Booking created successfully:', response);
      // Optionally, navigate to a different page after successful booking
    }, (error) => {
      console.error('Error creating booking:', error);
    });
  }

}
