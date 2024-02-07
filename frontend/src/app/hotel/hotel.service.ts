import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HotelService {
  baseUrl = 'http://localhost:5000'; 

  constructor(public http: HttpClient) {}


  getHotelData(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/hotels`);
  }


  getHotelDataWithAddress(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/hotelsWithAddress`);
  }


  HotelTsk(json: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/hotels`, { json });
  }


  HotelAddressTsk(json: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/hotelAddress`, { json });
  }
}
