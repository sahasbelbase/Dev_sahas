import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class InvoiceService {

  baseUrl = 'http://localhost:5500/api/Invoice/';
  constructor(
    public http :HttpClient
  ) { }

  GetInvoiceData(invoiceData: string): Observable<any> {
    const params = new HttpParams().set('json', '{}');
    return this.http.get(this.baseUrl + 'Invoice', { params});
  }
  // invoiceTsk(json:string): Observable<any>{
  //   return this.http.post(this.baseUrl + 'invoiceTsk', { json: json});
  // }
  
  }
  