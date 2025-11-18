class NotificationController < ApplicationController
  before_action :set_notification, only: [:show, :edit, :update, :destroy]

  # GET /notification
  def index
    @notifications = Notification.all
    render json: @notifications
  end

  # GET /notification/1
  def show
    render json: @notification
  end

  # POST /notification
  def create
    @notification = Notification.new(notification_params)

    if @notification.save
      render json: @notification, status: :created
    else
      render json: @notification.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /notification/1
  def update
    if @notification.update(notification_params)
      render json: @notification
    else
      render json: @notification.errors, status: :unprocessable_entity
    end
  end

  # DELETE /notification/1
  def destroy
    @notification.destroy
    head :no_content
  end

  private

  def set_notification
    @notification = Notification.find(params[:id])
  end

  def notification_params
    params.require(:notification).permit(:name)
  end
end
