import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { CustomerService } from '../customer.service';

@Component({
    selector: 'app-customerform',
    templateUrl: './customerform.component.html',
    styleUrls: ['./customerform.component.scss'],
    providers: [CustomerService]
})
export class CustomerFormComponent {
    customerObject = {
        person: { personId: 0 }, // Add a default person structure
        branchId: 0,
        userPersonId: ''
    };

    branchData: any;
    personData: any;

    constructor(
        public dialogRef: MatDialogRef<CustomerFormComponent>,
        @Inject(MAT_DIALOG_DATA) public data: any,
        public customerService: CustomerService
    ) {}

    ngOnInit(): void {
        this.customerService.getPersonData().subscribe((res: any) => {
            this.personData = res;
        });

        // Add the following line to fetch branch data
        this.customerService.getBranches().subscribe((res: any) => {
            this.branchData = res;
        });
    }

    submit(): void {
        console.log(this.customerObject); // Check if the object is populated correctly
        this.customerService.createCustomer(this.customerObject).subscribe((res) => {
            if (res) {
                this.dialogRef.close(res);
            }
        });
    }
}
