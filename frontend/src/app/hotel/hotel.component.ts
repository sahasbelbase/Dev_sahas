import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { HotelFormComponent } from './hotel-form/hotel-form.component';
import { HotelService } from './hotel.service';

@Component({
  selector: 'app-hotel',
  templateUrl: './hotel.component.html',
  styleUrls: ['./hotel.component.scss']
})
export class HotelComponent implements OnInit { 
  hotelData: any;
  typeData: any;
  constructor(
    public dialog:MatDialog,
    public hs:HotelService
  ){ }

  ngOnInit(): void{
    this.getHotelData();

    console.log('ngoninit');
    this.hotelData;
  }
  getHotelData(){
    let json = {};
    this.hs.GetHotelData(JSON.stringify(json)).subscribe(res =>{
      if (res) {
        this.hotelData = res.hotelData;
        this.typeData = res.typeData
      }
    });
  }
  add(): void {
    const dialogRef = this.dialog.open(HotelFormComponent, {
      data: {
        data: this.typeData,
        action: 'submit'
      }
      
    });
//listens anything that is closed
    dialogRef.afterClosed().subscribe(res => {
      if (res) {
        console.log('response');
        console.log(res);
        // res['hotelID'] = this.hotelData.length +1;
        // this.hotelData.push(res);
        this.getHotelData();

      }
      
      console.log('closed');
    });
    
  }
  edit(item: any,index:number) {
    const dialogRef = this.dialog.open(HotelFormComponent,{
      data: {
        data: item,
        action: 'edit'
      }
    });
    dialogRef.afterClosed().subscribe(res => {
      if(res) {
        this.hotelData[index] = res;
        this.getHotelData();
    }
    console.log('closed');
    });
  }
  delete(i:number): void{

      this.hotelData.splice(i, 1)
    }

  }
