import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HotelModule } from './hotel/hotel.module';
import { CustomerModule } from './customer/customer.module';
import { BranchModule } from './branch/branch.module';
import { NavigationModule } from './navigation/navigation.module';
import { InvoiceModule } from './invoice/invoice.module';
import { MatIconModule } from '@angular/material/icon'; // Add this import



@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HotelModule,
    CustomerModule,
    BranchModule,
    NavigationModule,
    InvoiceModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
