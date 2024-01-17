import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { CustomerformComponent } from './customerform/customerform.component';
import { customerService } from './customer.service';

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.scss']
})
export class CustomerComponent implements OnInit{
  customerData: any;
  branchData: any;
  personData: any;


constructor(
  public dialog:MatDialog,
  public hs: customerService
){}
ngOnInit(): void{
  this.getCustomerData();
}
getCustomerData():void{
  this.hs.GetCustomerData(JSON.stringify(this.customerData)).subscribe(res =>{
    if (res) {
      this.customerData = res.customerData;
      this.branchData = res.branchData;
      this.personData = res.personData;
    }
  });
}
add():void{
  const dialogRef = this.dialog.open(CustomerformComponent,{
    data:{
      data:this.branchData,
      data2:this.personData,
      mode:'add'
    }
  });
  dialogRef.afterClosed().subscribe(res =>{
    if(res) {
     this.getCustomerData();
    }
  });
}
}
