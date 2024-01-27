
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
    public dialog: MatDialog,
    public hs: HotelService
  ) {}

  ngOnInit(): void {
    this.getHotelData();
  }

  getHotelData(): void {
    this.hs.getHotelDataWithAddress().subscribe(res => {
      if (res) {
        this.hotelData = res;
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

    dialogRef.afterClosed().subscribe(res => {
      if (res) {
        this.hs.HotelTsk(JSON.stringify(res)).subscribe(result => {
          console.log(result);
          this.getHotelData();
        });
      }
    });
  }

  edit(item: any, index: number): void {
    const dialogRef = this.dialog.open(HotelFormComponent, {
      data: {
        data: item,
        action: 'edit'
      }
    });

    dialogRef.afterClosed().subscribe(res => {
      if (res) {
        this.hotelData[index] = res;
        this.getHotelData();
      }
    });
  }

  delete(i: number): void {
    this.hotelData.splice(i, 1);
  }
}
