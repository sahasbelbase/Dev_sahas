import { Component, Inject } from '@angular/core';
import { InvoiceService } from '../invoice.service';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-invoice-form',
  templateUrl: './invoice-form.component.html',
  styleUrls: ['./invoice-form.component.scss']
})
export class InvoiceFormComponent {
  invoiceData: any;

  constructor(
    public dialogRef: MatDialogRef<InvoiceFormComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    public hs: InvoiceService
  ) {
    this.invoiceData = data.invoiceData;
  }

  closeInvoice(): void {
    this.dialogRef.close();
  }
}