import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { BranchFormComponent } from './branch-form/branch-form.component';
import { BranchService } from './branch.service';

@Component({
  selector: 'app-branch',
  templateUrl: './branch.component.html',
  styleUrls: ['./branch.component.scss']
})
export class BranchComponent implements OnInit {
  branchData: any;
  hotelData: any;
  typeData: any;
  constructor(
    public dialog: MatDialog,
    public hs: BranchService
  ) {}

  ngOnInit(): void {
    this.getBranchData();
    console.log('ngoninit');
    this.branchData;
  }

  getBranchData(): void {
    let json = {};
    this.hs.GetBranchData(JSON.stringify(json)).subscribe(res => {
      if (res) {
        this.branchData = res.branchData;
        this.hotelData = res.hotelData;
        this.typeData = res.typeData;

        // Map hotelName to branchData based on hotelId
        // this.branchData.forEach((branch: any) => {
        //   const matchingHotel = this.hotelData.find((hotel: any) => hotel.hotelId === branch.hotelId);
        //   if (matchingHotel) {
        //     branch.name = matchingHotel.name;
        //   }
        // });
      }
    });
  }

  add(): void {
    const dialogRef = this.dialog.open(BranchFormComponent, {
      data: {
        data: this.hotelData,
        data1: this.typeData,
        action: 'submit'
      }
    });

    dialogRef.afterClosed().subscribe(res => {
      if (res) {
        // res['branchId'] = this.branchData.length + 1;
        // this.branchData.push(res);
        this.getBranchData();
      }
    });
  }
  edit(item: any,index:number) {
    const dialogRef = this.dialog.open(BranchFormComponent,{
      data: {
        data: item,
        action: 'edit'
      }
    });
    dialogRef.afterClosed().subscribe(res => {
      if(res) {
        this.branchData[index] = res;
        this.getBranchData();
    }
    console.log('closed');
    });
  }
}
