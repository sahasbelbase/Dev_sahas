// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CommonModule } from '@angular/common';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HotelModule } from './hotel/hotel.module';
import { RouterModule } from '@angular/router'; 
import { CustomerModule } from './customer/customer.module';
import { BranchModule } from './branch/branch.module';
import { NavigationModule } from './navigation/navigation.module';
import { InvoiceModule } from './invoice/invoice.module';
import { MatIconModule } from '@angular/material/icon';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { RoomModule } from './room/room.module';
import { BookingModule } from './booking/booking.module';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    CommonModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HotelModule,
    CustomerModule,
    BranchModule,
    NavigationModule,
    InvoiceModule,
    RoomModule,
    BookingModule,
    RouterModule.forRoot([]), // Import and configure RouterModule
    MatIconModule,
    ReactiveFormsModule,
    FormsModule,
      ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
