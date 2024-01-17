import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class customerService {

  baseUrl = 'http://localhost:5500/api/Customer/';
  constructor(
    public http :HttpClient
  ) { }

  GetCustomerData(customerData: string): Observable<any> {
    const params = new HttpParams().set('json', '{}');
    return this.http.get(this.baseUrl + 'Customer', { params});
  }
  CustomerTsk(json:string): Observable<any>{
    return this.http.post(this.baseUrl + 'CustomerTsk', { json: json});
  }
  
  }
  