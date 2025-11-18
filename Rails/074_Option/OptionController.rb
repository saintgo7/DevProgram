class OptionController < ApplicationController
  before_action :set_option, only: [:show, :edit, :update, :destroy]

  # GET /option
  def index
    @options = Option.all
    render json: @options
  end

  # GET /option/1
  def show
    render json: @option
  end

  # POST /option
  def create
    @option = Option.new(option_params)

    if @option.save
      render json: @option, status: :created
    else
      render json: @option.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /option/1
  def update
    if @option.update(option_params)
      render json: @option
    else
      render json: @option.errors, status: :unprocessable_entity
    end
  end

  # DELETE /option/1
  def destroy
    @option.destroy
    head :no_content
  end

  private

  def set_option
    @option = Option.find(params[:id])
  end

  def option_params
    params.require(:option).permit(:name)
  end
end
