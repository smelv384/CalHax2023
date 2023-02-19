package com.example.campuscushion.domain.main;

public interface RoomRepository {
    List<Room> getAvailableRoomsForTimeSlot(String timeSlot) throws RoomRepositoryException;

    public class RoomRepositoryException extends Exception {
        public RoomRepositoryException(String message, Throwable cause) {
            super(message, cause);
        }

        public RoomRepositoryException(String message) {
            super(message);
        }
    }
}


