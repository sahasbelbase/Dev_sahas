// customer.service.ts

import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {
  baseUrl = 'http://localhost:5000/';

  constructor(private http: HttpClient) {}

  getCustomers(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/customers`);
  }
 
  createCustomer(customerData: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/customers`, customerData);
  }

  getPersonData(): Observable<any> {
    return this.http.get(`${this.baseUrl}/persons`);
  }

  getBranches(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/branches`);
  }
}
