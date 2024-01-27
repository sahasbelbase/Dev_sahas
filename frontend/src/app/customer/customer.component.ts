import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { CustomerFormComponent } from './customerform/customerform.component';
import { CustomerService } from './customer.service';

@Component({
  selector: 'app-customer',
  templateUrl: './customer.component.html',
  styleUrls: ['./customer.component.scss'],
  providers: [CustomerService] 
})
export class CustomerComponent implements OnInit {
  customerData: any;

  constructor(public dialog: MatDialog, public customerService: CustomerService) {}

  ngOnInit(): void {
    this.getCustomerData();
  }

  getCustomerData(): void {
    this.customerService.getCustomers().subscribe((res) => {
      if (res) {
        this.customerData = res;
      }
    });
  }

  add(): void {
    const dialogRef = this.dialog.open(CustomerFormComponent, {
      data: {
        data: this.customerData,
        mode: 'add'
      }
    });

    dialogRef.afterClosed().subscribe((res) => {
      if (res) {
        this.getCustomerData();
      }
    });
  }
}
