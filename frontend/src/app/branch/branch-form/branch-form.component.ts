// src/app/branch/branch-form/branch-form.component.ts

import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { BranchService } from '../branch.service';

@Component({
  selector: 'app-branch-form',
  templateUrl: './branch-form.component.html',
  styleUrls: ['./branch-form.component.scss']
})
export class BranchFormComponent implements OnInit {
  branchObject = {
    branchId: 0,
    hotelId: 0,
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
  ) {}

  ngOnInit(): void {
    if (this.data.action == 'edit') {
      this.branchObject = { ...this.data.data };
    }
    this.typeData = this.data.data1;
    this.hotelData = this.data.data;
  }

  submit(): void {
    console.log('from submit');
    console.log(this.branchObject);
    let json = {
      branchData: this.branchObject,
      action: this.data.action
    };
    // Use the correct method name: branchTask
    this.hs.branchTask(JSON.stringify(json)).subscribe((res: any) => {
      if (res) {
        this.dialogRef.close(res);
      }
    });
    // Note: You don't need to close the dialogRef here again; it's already closed in the subscribe callback.
  }
}
