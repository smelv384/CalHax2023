package com.example.campuscushion.domain.main;

public class GetAvailableRoomsUseCase {
    private final RoomRepository roomRepository;

    public GetAvailableRoomsUseCase(RoomRepository roomRepository) {
        this.roomRepository = roomRepository;
    }

    public List<Room> getAvailableRooms(String timeSlot) throws RoomRepositoryException {
        try {
            return roomRepository.getAvailableRoomsForTimeSlot(timeSlot);
        } catch (RoomRepository.RoomRepositoryException e) {
            throw new RuntimeException(e.getMessage(), e);
        }
    }
}
