import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InvoiceService {
  baseUrl = 'http://localhost:5000';

  constructor(public http: HttpClient) {}

  GetInvoiceData(): Observable<any> {
    return this.http.get(`${this.baseUrl}/invoices`);
  }

  invoiceAction(json: string, action: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/invoices`, { json: json, action: action });
  }

  getCustomerName(customerId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/getCustomerName/${customerId}`);
  }

  getBranchName(userPersonId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/getBranchName/${userPersonId}`);
  }

  GetInvoicesWithDetails(): Observable<any> {
    return this.http.get(`${this.baseUrl}/invoices-with-details`);
  }

}