class RealTimeController < ApplicationController
  before_action :set_realtime, only: [:show, :edit, :update, :destroy]

  # GET /realtime
  def index
    @realtimes = RealTime.all
    render json: @realtimes
  end

  # GET /realtime/1
  def show
    render json: @realtime
  end

  # POST /realtime
  def create
    @realtime = RealTime.new(realtime_params)

    if @realtime.save
      render json: @realtime, status: :created
    else
      render json: @realtime.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /realtime/1
  def update
    if @realtime.update(realtime_params)
      render json: @realtime
    else
      render json: @realtime.errors, status: :unprocessable_entity
    end
  end

  # DELETE /realtime/1
  def destroy
    @realtime.destroy
    head :no_content
  end

  private

  def set_realtime
    @realtime = RealTime.find(params[:id])
  end

  def realtime_params
    params.require(:realtime).permit(:name)
  end
end
