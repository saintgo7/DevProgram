class BookingController < ApplicationController
  before_action :set_booking, only: [:show, :edit, :update, :destroy]

  # GET /booking
  def index
    @bookings = Booking.all
    render json: @bookings
  end

  # GET /booking/1
  def show
    render json: @booking
  end

  # POST /booking
  def create
    @booking = Booking.new(booking_params)

    if @booking.save
      render json: @booking, status: :created
    else
      render json: @booking.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /booking/1
  def update
    if @booking.update(booking_params)
      render json: @booking
    else
      render json: @booking.errors, status: :unprocessable_entity
    end
  end

  # DELETE /booking/1
  def destroy
    @booking.destroy
    head :no_content
  end

  private

  def set_booking
    @booking = Booking.find(params[:id])
  end

  def booking_params
    params.require(:booking).permit(:name)
  end
end
