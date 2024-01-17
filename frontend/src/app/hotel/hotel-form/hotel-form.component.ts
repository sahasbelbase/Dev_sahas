import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { HotelService } from '../hotel.service';

@Component({
  selector: 'app-hotel-form',
  templateUrl: './hotel-form.component.html',
  styleUrls: ['./hotel-form.component.scss']
})
export class HotelFormComponent implements OnInit {
  hotelObject = {
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
    if(this.data.action=='edit')
    {
      this.hotelObject = {...this.data.data};
    }
    this.typeData = this.data.data;
  }
// 
  submit (): void {
    console.log('from submit');
    console.log(this.hotelObject);
    let json = {
      hotelData:this.hotelObject,
      action:this.data.action
    }
    this.hs.HotelTsk(JSON.stringify(json)).subscribe(res =>{
      if(res) {
        this.dialogRef.close(res);
      }
    });
    this.dialogRef.close(this.hotelObject);
  }
}
