class FieldController < ApplicationController
  before_action :set_field, only: [:show, :edit, :update, :destroy]

  # GET /field
  def index
    @fields = Field.all
    render json: @fields
  end

  # GET /field/1
  def show
    render json: @field
  end

  # POST /field
  def create
    @field = Field.new(field_params)

    if @field.save
      render json: @field, status: :created
    else
      render json: @field.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /field/1
  def update
    if @field.update(field_params)
      render json: @field
    else
      render json: @field.errors, status: :unprocessable_entity
    end
  end

  # DELETE /field/1
  def destroy
    @field.destroy
    head :no_content
  end

  private

  def set_field
    @field = Field.find(params[:id])
  end

  def field_params
    params.require(:field).permit(:name)
  end
end
