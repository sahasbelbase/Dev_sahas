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
    // Logic to calculate price and days based on check-in and check-out dates
    // Then submit the booking form
    this.bookingService.createBooking(this.bookingForm.value).subscribe((response: any) => {
      console.log('Booking created successfully:', response);
      // Optionally, navigate to a different page after successful booking
    }, (error) => {
      console.error('Error creating booking:', error);
    });
  }
}
