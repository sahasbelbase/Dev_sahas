import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { BranchService } from '../branch.service';

@Component({
  selector: 'app-branch-form',
  templateUrl: './branch-form.component.html',
  styleUrls: ['./branch-form.component.scss'],
})
export class BranchFormComponent {
  formData: any = {}; 

  hotelData: any[] = []; 
  addressTypes: any[] = []; 

  constructor(private branchService: BranchService) {}

  ngOnInit(): void {
    // Fetch necessary data for dropdowns, e.g., hotelData, addressTypes
    this.branchService.getHotels().subscribe((hotels) => {
      this.hotelData = hotels;
    });

    this.branchService.getAddressTypes().subscribe((types) => {
      this.addressTypes = types;
    });
  }

  onSubmit() {
    // Implement logic to submit the form data to the server
    
    this.branchService.addBranch(this.formData).subscribe(
      (response) => {
        
        console.log('Form submitted successfully:', response);
      },
      (error) => {
        
        console.error('Error submitting form:', error);
      }
    );
  }
}
