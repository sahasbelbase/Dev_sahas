// booking.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { BookingComponent } from './booking.component';
import { BookingService } from './booking.service'; // Import the service

@NgModule({
  declarations: [
    BookingComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [BookingService] // Provide the service here
})
export class BookingModule { }
