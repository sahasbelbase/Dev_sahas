import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RoomService {
  private baseUrl = 'http://localhost:5000'; // Update with your API base URL

  constructor(private http: HttpClient) { }

  getRoomAvailability(): Observable<any> {
    return this.http.get(`${this.baseUrl}/room_availability`);
  }
}
