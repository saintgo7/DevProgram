class SchemaController < ApplicationController
  before_action :set_schema, only: [:show, :edit, :update, :destroy]

  # GET /schema
  def index
    @schemas = Schema.all
    render json: @schemas
  end

  # GET /schema/1
  def show
    render json: @schema
  end

  # POST /schema
  def create
    @schema = Schema.new(schema_params)

    if @schema.save
      render json: @schema, status: :created
    else
      render json: @schema.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /schema/1
  def update
    if @schema.update(schema_params)
      render json: @schema
    else
      render json: @schema.errors, status: :unprocessable_entity
    end
  end

  # DELETE /schema/1
  def destroy
    @schema.destroy
    head :no_content
  end

  private

  def set_schema
    @schema = Schema.find(params[:id])
  end

  def schema_params
    params.require(:schema).permit(:name)
  end
end
