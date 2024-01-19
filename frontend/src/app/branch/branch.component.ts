// src/app/branch/branch.component.ts

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
  branchData: any[] = [];

  constructor(public dialog: MatDialog, public branchService: BranchService) {}

  ngOnInit(): void {
    this.getBranchData();
  }

  getBranchData(): void {
    this.branchService.getAllBranches().subscribe((data: any) => {
      this.branchData = data;
    });
  }

  add(): void {
    const dialogRef = this.dialog.open(BranchFormComponent, {
      data: {
        action: 'submit'
      } as any  // Resolve TypeScript error - Parameter 'data' implicitly has an 'any' type.
    });

    dialogRef.afterClosed().subscribe((res: any) => {
      if (res) {
        this.getBranchData();
      }
    });
  }

  edit(item: any, index: number): void {
    const dialogRef = this.dialog.open(BranchFormComponent, {
      data: {
        data: item,
        action: 'edit'
      } as any  // Resolve TypeScript error - Parameter 'data' implicitly has an 'any' type.
    });

    dialogRef.afterClosed().subscribe((res: any) => {
      if (res) {
        this.branchData[index] = res;
        this.getBranchData();
      }
    });
  }
}
