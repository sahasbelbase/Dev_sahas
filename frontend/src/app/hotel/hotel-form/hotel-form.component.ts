import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { HotelService } from '../hotel.service';

// Define the HotelObject interface
interface HotelObject {
  hotelId: number;
  addressTypeId: string;
  name: string;
  country: string;
  city: string;
  streetName: string;
  pan: string;
  userPersonId: string;
}

@Component({
  selector: 'app-hotel-form',
  templateUrl: './hotel-form.component.html',
  styleUrls: ['./hotel-form.component.scss']
})
export class HotelFormComponent implements OnInit {
  // Initialize hotelObject as an instance of HotelObject
  hotelObject: HotelObject = {
    hotelId: 0,
    addressTypeId: '',
    name: '',
    country: '',
    city: '',
    streetName: '',
    pan: '',
    userPersonId: ''
  };

  typeData: any;

  constructor(
    public dialogRef: MatDialogRef<HotelFormComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    public hs: HotelService
  ) {}

  ngOnInit(): void {
    console.log('Type Data:', this.typeData); 
    if (this.data.action === 'edit') {
      this.hotelObject = { ...this.data.data };
    }
    this.typeData = this.data.data;
  }

  submit(): void {
    let json = {
      hotelData: this.hotelObject,
      action: this.data.action
    };

    this.hs.HotelTsk(JSON.stringify(json)).subscribe(res => {
      if (res) {
        this.dialogRef.close(res);
      }
    });
  }
}
