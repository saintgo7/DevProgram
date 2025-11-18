class TableController < ApplicationController
  before_action :set_table, only: [:show, :edit, :update, :destroy]

  # GET /table
  def index
    @tables = Table.all
    render json: @tables
  end

  # GET /table/1
  def show
    render json: @table
  end

  # POST /table
  def create
    @table = Table.new(table_params)

    if @table.save
      render json: @table, status: :created
    else
      render json: @table.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /table/1
  def update
    if @table.update(table_params)
      render json: @table
    else
      render json: @table.errors, status: :unprocessable_entity
    end
  end

  # DELETE /table/1
  def destroy
    @table.destroy
    head :no_content
  end

  private

  def set_table
    @table = Table.find(params[:id])
  end

  def table_params
    params.require(:table).permit(:name)
  end
end
