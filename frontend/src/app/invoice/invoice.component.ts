import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { InvoiceService } from './invoice.service';
import { InvoiceFormComponent } from './invoice-form/invoice-form.component';

@Component({
  selector: 'app-invoice',
  templateUrl: './invoice.component.html',
  styleUrls: ['./invoice.component.scss']
})
export class InvoiceComponent implements OnInit {
  invoiceData: any;

  constructor(
    public dialog: MatDialog,
    public hs: InvoiceService
  ) { }

  ngOnInit(): void {
    this.getInvoiceData();
  }

  getInvoiceData(): void {
    this.hs.GetInvoiceData().subscribe((res: any) => {
      if (res) {
        this.invoiceData = res.map((item: any) => {
          return {
            ...item,
            customerName: this.getCustomerName(item.customerId),
            branchName: this.getBranchName(item.userPersonId)
          };
        });
      }
    });
  }

  getCustomerName(customerId: number): string {
    return `Customer ${customerId}`;
  }

  getBranchName(branchName: string): string {

    return `Branch ${branchName}`;
  }

  display(item: any): void {
    const dialogRef = this.dialog.open(InvoiceFormComponent, {
      data: {
        invoiceData: item
      }
    });
  }
}
