import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HotelComponent } from './hotel/hotel.component';
import { CustomerComponent } from './customer/customer.component';
import { BranchComponent } from './branch/branch.component';
import { InvoiceComponent } from './invoice/invoice.component';
import { RoomComponent } from './room/room.component'; 
import { BookingComponent } from './booking/booking.component';

const routes: Routes = [
  { path: 'hotel', component: HotelComponent },
  { path: '', component: HotelComponent, pathMatch: 'full' },
  { path: 'customer', component: CustomerComponent },
  { path: 'branch', component: BranchComponent },
  { path: 'invoice', component: InvoiceComponent },
  { path: 'room', component: RoomComponent },
  { path: 'booking/:roomId', component: BookingComponent } // Include the roomId parameter
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
