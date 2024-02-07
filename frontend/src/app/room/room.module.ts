import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RoomComponent } from './room.component';
import { MatIconModule } from '@angular/material/icon'; // Import MatIconModule

@NgModule({
  declarations: [
    RoomComponent
  ],
  imports: [
    CommonModule,
    MatIconModule // Add MatIconModule to imports array
  ]
})
export class RoomModule { }
