import { Component, Inject,OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { BranchService } from '../branch.service';

@Component({
  selector: 'app-branch-form',
  templateUrl: './branch-form.component.html',
  styleUrls: ['./branch-form.component.scss']
})
export class BranchFormComponent implements OnInit{
  branchObject =   
    {branchId:0,
      hotelId:0,
      addressTypeId: '',
      name: '',
      branchName: '',
      country: '',
      city: '',
      streetName: '',
      userPersonId: ''
    };
  typeData: any;
  hotelData: any;
  constructor(
    public dialogRef: MatDialogRef<BranchFormComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    public hs: BranchService
  ){

  }
  ngOnInit():void{
    if(this.data.action=='edit')
    {
      this.branchObject = {...this.data.data};
    }
    this.typeData = this.data.data1;
    this.hotelData = this.data.data;
  }
  submit(){
    console.log('from submit');
    console.log(this.branchObject);
    let json = {
      branchData:this.branchObject,
      action:this.data.action
    }
    this.hs.BranchTsk(JSON.stringify(json)).subscribe(res =>{
      if(res) {
        this.dialogRef.close(res);
      }
    });
    this.dialogRef.close(this.branchObject)
  }
}
