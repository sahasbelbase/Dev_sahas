import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BookingService {
  private baseUrl = 'http://localhost:5000'; // Update with your API base URL

  constructor(private http: HttpClient) { }

  getCustomers(): Observable<any> {
    return this.http.get(`${this.baseUrl}/customers`);
  }

  createBooking(bookingData: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/bookings`, bookingData);
  }
}
