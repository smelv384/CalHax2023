package com.example.campuscushion.data.main;

import com.example.campuscushion.domain.main.RoomRepository;
import com.apollographql.apollo3.cache.normalized.NormalizedCache;
import com.apollographql.apollo3.cache.http.HttpCache;
import com.apollographql.apollo3.rx2.Rx2Apollo;

public class ApolloRoomRepository implements RoomRepository {
    private final ApolloClient apolloClient = ApolloClient.builder()
            .serverUrl("https://example.com/graphql")
            .build();

    @Override
    public List<Room> getAvailableRoomsForTimeSlot(String timeSlot) throws RoomRepositoryException {
        ApolloClient.Builder builder = new ApolloClient.Builder()
                .serverUrl("http://localhost:4000/graphql");

        // Optionally, set an http cache
        // HttpCache.configureApolloClientBuilder(builder, cacheDirectory, cacheMaxSize);

        // Optionally, set a normalized cache
        NormalizedCache.configureApolloClientBuilder(
                builder,
                new MemoryCacheFactory(10 * 1024 * 1024, -1),
                TypePolicyCacheKeyGenerator.INSTANCE,
                FieldPolicyCacheResolver.INSTANCE,
                false
        );

        ApolloClient client = builder.build();
        // ----
        // Query
        ApolloCall<MyQuery.Data> queryCall = client.query(new MyQuery());
        Single<ApolloResponse<MyQuery.Data>> queryResponse = Rx2Apollo.single(queryCall);
        queryResponse.subscribe( /* myObserver */);

        // Mutation
        ApolloCall<MyMutation.Data> mutationCall = client.mutation(new MyMutation("my-parameter"));
        Single<ApolloResponse<MyMutation.Data>> mutationResponse = Rx2Apollo.single(mutationCall);
        mutationResponse.subscribe( /* ... */ );

        // Subscription
        ApolloCall<MySubscription.Data> subscriptionCall = client.subscription(new MySubscription());
        Flowable<ApolloResponse<MySubscription.Data>> subscriptionResponse = Rx2Apollo.flowable(subscriptionCall);
        subscriptionResponse.subscribe( /* ... */ );

        /*
//        GetAvailableRoomsQuery query = GetAvailableRoomsQuery.builder()
//                .timeSlot(timeSlot)
//                .build();

        Response<GetAvailableRoomsQuery.Data> response;
        try {
            response = apolloClient.query(query).execute();
        } catch (ApolloException e) {
            throw new RoomRepositoryException("Failed to retrieve available rooms for time slot " + timeSlot, e);
        }

        if (response.hasErrors()) {
            String errorMessage = response.errors().stream()
                    .map(Error::getMessage)
                    .collect(Collectors.joining("\n"));
            throw new RoomRepositoryException("GraphQL query returned errors: " + errorMessage);
        }

        List<Room> availableRooms = new ArrayList<>();
        if (response.getData() != null && response.getData().rooms() != null) {
            for (Room room : response.getData().rooms()) {
                List<TimeSlot> schedule = room.schedule();
                if (schedule == null || schedule.stream().noneMatch(ts -> timeSlot.equals(ts.timeSlot()))) {
                    availableRooms.add(room);
                }
            }
        }
        return availableRooms;

         */
    }
}

