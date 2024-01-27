import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { BranchService } from './branch.service';
import { Branch } from './branch.model';
import { BranchFormComponent } from './branch-form/branch-form.component';

@Component({
  selector: 'app-branch',
  templateUrl: './branch.component.html',
  styleUrls: ['./branch.component.scss'],
})
export class BranchComponent implements OnInit {
  branchData: Branch[] = [];
  hotelData: any[] = [];
  typeData: any[] = [];

  constructor(private branchService: BranchService, public dialog: MatDialog) {}

  ngOnInit(): void {
    this.loadBranches();
  }

  

  loadBranches() {
    this.branchService.getBranchesWithAddress().subscribe(
      (branches) => {
        this.branchData = branches;
      },
      (error) => {
        console.error('Error loading branches:', error);
      }
    );
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
        this.getBranchData();
      }
    });
  }

  edit(item: any, index: number) {
    const dialogRef = this.dialog.open(BranchFormComponent, {
      data: {
        data: item,
        action: 'edit'
      }
    });

    dialogRef.afterClosed().subscribe(res => {
      if (res) {
        this.branchData[index] = res;
        this.getBranchData();
      }
    });
  }

  private getBranchData() {
    this.branchService.getBranchesWithAddress().subscribe(
      (branches) => {
        this.branchData = branches;
      },
      (error) => {
        console.error('Error loading branches:', error);
      }
    );
  }
}
