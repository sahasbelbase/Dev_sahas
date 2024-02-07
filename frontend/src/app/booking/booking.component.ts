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
    this.roomId = this.route.snapshot.queryParams['roomId']; // Get roomId from route
    this.loadCustomers();
  }

  loadCustomers() {
    this.bookingService.getCustomers().subscribe((data: any) => {
      this.customers = data;
    }, (error) => {
      console.error('Error fetching customers:', error);
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
  
    // Calculate the price based on the number of days and any other relevant factors
    const pricePerDay = 100; // Example price per day
    const totalPrice = numberOfDays * pricePerDay;
  
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
