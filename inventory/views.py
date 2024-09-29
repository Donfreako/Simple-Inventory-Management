from rest_framework import generics,status
from rest_framework.response import Response
from .models import Item
from rest_framework.views import APIView
from .serializers import ItemSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .utils import get_cache, set_cache
from django.core.cache import cache
import logging

logger = logging.getLogger('management_system')

class RegisterView(generics.CreateAPIView):
    logger.info("Registering a new user")
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ItemCreateView(APIView):
    def post(self, request):
        logger.info("Creating a new item")
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            if Item.objects.filter(name=serializer.validated_data['name']).exists():
                logger.warning("Attempt to create an item that already exists")
                return Response({"error": "Item already exists"}, status=status.HTTP_400_BAD_REQUEST)
            item = serializer.save()
            logger.info(f"Item created successfully: {item.id}")
            return Response(ItemSerializer(item).data, status=status.HTTP_201_CREATED)
        logger.error("Error creating item: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request, *args, **kwargs):
        logger.info("Listing all items")
        return super().list(request, *args, **kwargs)

class ItemView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        logger.info(f"Fetching item with id: {item_id}")
        cache_key = f'item_{item_id}'
        item_data = get_cache(cache_key)
        item = get_object_or_404(Item,id=item_id)
        serializer = ItemSerializer(item)
        set_cache(cache_key, item_data)
        return Response(serializer.data)
    
    def put(self, request, item_id):
        logger.info(f"Updating item with id: {item_id}")
        item = get_object_or_404(Item, id=item_id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache_key = f'item_{item_id}'
            set_cache(cache_key, serializer.data)
            logger.info(f"Item updated successfully: {item_id}")
            return Response(serializer.data)
        logger.error("Error updating item: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, item_id):
        logger.info(f"Deleting item with id: {item_id}")
        item = get_object_or_404(Item,id=item_id)
        item.delete()
        cache_key = f'item_{item_id}'
        cache.delete(cache_key)
        logger.info(f"Item deleted successfully: {item_id}")
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    