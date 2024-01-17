import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { customerService } from '../customer.service';
@Component({
  selector: 'app-customerform',
  templateUrl: './customerform.component.html',
  styleUrls: ['./customerform.component.scss']
})
export class CustomerformComponent {
  customerObject = {
    personId: 0,
    branchId: 0,
    userPersonId: ''
  }
  branchData: any;
  personData: any;
  constructor(
    public dialogRef: MatDialogRef<CustomerformComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    public hs: customerService
  ){}
  ngOnInit():void{
    this.branchData = this.data.data;
    this.personData = this.data.data2;
  }
  submit(){
    console.log('from submit')
    console.log(this.customerObject)
    this.hs.CustomerTsk(JSON.stringify(this.customerObject)).subscribe(res =>{
      if(res) {
        this.dialogRef.close(res);
      }
    });
    this.dialogRef.close(this.customerObject)
  }
}
