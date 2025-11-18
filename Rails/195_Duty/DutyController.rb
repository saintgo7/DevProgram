class DutyController < ApplicationController
  before_action :set_duty, only: [:show, :edit, :update, :destroy]

  # GET /duty
  def index
    @dutys = Duty.all
    render json: @dutys
  end

  # GET /duty/1
  def show
    render json: @duty
  end

  # POST /duty
  def create
    @duty = Duty.new(duty_params)

    if @duty.save
      render json: @duty, status: :created
    else
      render json: @duty.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /duty/1
  def update
    if @duty.update(duty_params)
      render json: @duty
    else
      render json: @duty.errors, status: :unprocessable_entity
    end
  end

  # DELETE /duty/1
  def destroy
    @duty.destroy
    head :no_content
  end

  private

  def set_duty
    @duty = Duty.find(params[:id])
  end

  def duty_params
    params.require(:duty).permit(:name)
  end
end
