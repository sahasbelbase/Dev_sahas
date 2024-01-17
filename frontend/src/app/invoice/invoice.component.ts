import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { InvoiceService} from './invoice.service';
import { InvoiceFormComponent } from './invoice-form/invoice-form.component';


@Component({
  selector: 'app-invoice',
  templateUrl: './invoice.component.html',
  styleUrls: ['./invoice.component.scss']
})
export class InvoiceComponent implements OnInit{
  invoiceData: any; 
  // branchData: any;
  // customerData: any;
constructor(
  public dialog:MatDialog,
  public hs: InvoiceService
){}
ngOnInit(): void{
  this.getInvoiceData();
}
getInvoiceData():void{
  this.hs.GetInvoiceData(JSON.stringify(JSON)).subscribe((res: any) =>{
    if (res) {
      this.invoiceData = res; 
      // this.branchData = res.branchData;
      // this.customerData = res.customerData; 
    }
  }); 
}
display(item:any){
  const dialogRef = this.dialog.open(InvoiceFormComponent,{
    data:{
      data:item
    }
  });

}
}
