class SMSController < ApplicationController
  before_action :set_sms, only: [:show, :edit, :update, :destroy]

  # GET /sms
  def index
    @smss = SMS.all
    render json: @smss
  end

  # GET /sms/1
  def show
    render json: @sms
  end

  # POST /sms
  def create
    @sms = SMS.new(sms_params)

    if @sms.save
      render json: @sms, status: :created
    else
      render json: @sms.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /sms/1
  def update
    if @sms.update(sms_params)
      render json: @sms
    else
      render json: @sms.errors, status: :unprocessable_entity
    end
  end

  # DELETE /sms/1
  def destroy
    @sms.destroy
    head :no_content
  end

  private

  def set_sms
    @sms = SMS.find(params[:id])
  end

  def sms_params
    params.require(:sms).permit(:name)
  end
end
