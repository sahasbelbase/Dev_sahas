import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HotelService {
  baseUrl = 'http://localhost:5000'; 

  constructor(public http: HttpClient) {}

  // Fetch hotel data
  getHotelData(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/hotels`);
  }

  // Fetch hotel data with address information
  getHotelDataWithAddress(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/hotelsWithAddress`);
  }

  // Handle hotel task (create/update)
  HotelTsk(json: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/hotels`, { json });
  }

  // Handle hotel address task (create/update)
  HotelAddressTsk(json: string): Observable<any> {
    return this.http.post(`${this.baseUrl}/hotelAddress`, { json });
  }
}
