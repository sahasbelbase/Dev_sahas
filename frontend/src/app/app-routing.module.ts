import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HotelComponent } from './hotel/hotel.component';
import { CustomerComponent } from './customer/customer.component';
import { BranchComponent } from './branch/branch.component';
import { InvoiceComponent } from './invoice/invoice.component';
import { RoomComponent } from './room/room.component'; // Import the RoomComponent

const routes: Routes = [
  { path: 'hotel', component: HotelComponent },
  { path: '', component: HotelComponent, pathMatch: 'full' },
  { path: 'customer', component: CustomerComponent },
  { path: 'branch', component: BranchComponent },
  { path: 'invoice', component: InvoiceComponent },
  { path: 'room', component: RoomComponent } // Add the route for the RoomComponent
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
