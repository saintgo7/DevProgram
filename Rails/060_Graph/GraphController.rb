class GraphController < ApplicationController
  before_action :set_graph, only: [:show, :edit, :update, :destroy]

  # GET /graph
  def index
    @graphs = Graph.all
    render json: @graphs
  end

  # GET /graph/1
  def show
    render json: @graph
  end

  # POST /graph
  def create
    @graph = Graph.new(graph_params)

    if @graph.save
      render json: @graph, status: :created
    else
      render json: @graph.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /graph/1
  def update
    if @graph.update(graph_params)
      render json: @graph
    else
      render json: @graph.errors, status: :unprocessable_entity
    end
  end

  # DELETE /graph/1
  def destroy
    @graph.destroy
    head :no_content
  end

  private

  def set_graph
    @graph = Graph.find(params[:id])
  end

  def graph_params
    params.require(:graph).permit(:name)
  end
end
