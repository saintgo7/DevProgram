class BroadcastController < ApplicationController
  before_action :set_broadcast, only: [:show, :edit, :update, :destroy]

  # GET /broadcast
  def index
    @broadcasts = Broadcast.all
    render json: @broadcasts
  end

  # GET /broadcast/1
  def show
    render json: @broadcast
  end

  # POST /broadcast
  def create
    @broadcast = Broadcast.new(broadcast_params)

    if @broadcast.save
      render json: @broadcast, status: :created
    else
      render json: @broadcast.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /broadcast/1
  def update
    if @broadcast.update(broadcast_params)
      render json: @broadcast
    else
      render json: @broadcast.errors, status: :unprocessable_entity
    end
  end

  # DELETE /broadcast/1
  def destroy
    @broadcast.destroy
    head :no_content
  end

  private

  def set_broadcast
    @broadcast = Broadcast.find(params[:id])
  end

  def broadcast_params
    params.require(:broadcast).permit(:name)
  end
end
